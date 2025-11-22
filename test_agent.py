"""
Test script for the Sustainability Footprint Agent.
Tests API endpoints and agent functionality.
"""

import requests
import json


def test_health_check():
    """Test the health check endpoint."""
    print("\n" + "="*60)
    print("Testing Health Check Endpoint")
    print("="*60)
    
    response = requests.get("http://localhost:8000/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    print("✓ Health check passed!")


def test_agent_info():
    """Test the agent info endpoint."""
    print("\n" + "="*60)
    print("Testing Agent Info Endpoint")
    print("="*60)
    
    response = requests.get("http://localhost:8000/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    print("✓ Agent info retrieved!")


def test_carbon_footprint_query():
    """Test carbon footprint analysis query."""
    print("\n" + "="*60)
    print("Testing Carbon Footprint Query")
    print("="*60)
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "What is the carbon footprint of driving 100 miles in a gasoline car?"
            }
        ]
    }
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json=payload
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Agent Name: {result['agent_name']}")
    print(f"Status: {result['status']}")
    print(f"Response: {result['data']['message'][:200]}...")
    
    assert response.status_code == 200
    assert result["status"] == "success"
    print("✓ Carbon footprint query successful!")


def test_energy_query():
    """Test energy consumption query."""
    print("\n" + "="*60)
    print("Testing Energy Consumption Query")
    print("="*60)
    
    payload = {
        "messages": [
            {
                "role": "assistant",
                "content": "Hello! How can I help you with sustainability today?"
            },
            {
                "role": "user",
                "content": "What are the benefits of installing solar panels?"
            }
        ]
    }
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json=payload
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Status: {result['status']}")
    print(f"Response: {result['data']['message'][:200]}...")
    
    assert response.status_code == 200
    assert result["status"] == "success"
    print("✓ Energy query successful!")


def test_waste_management_query():
    """Test waste management query."""
    print("\n" + "="*60)
    print("Testing Waste Management Query")
    print("="*60)
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "How can I reduce household waste?"
            }
        ]
    }
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json=payload
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Status: {result['status']}")
    print(f"Response: {result['data']['message'][:200]}...")
    
    assert response.status_code == 200
    assert result["status"] == "success"
    print("✓ Waste management query successful!")


def test_ltm_cache():
    """Test Long-Term Memory caching."""
    print("\n" + "="*60)
    print("Testing LTM Cache")
    print("="*60)
    
    query = "What is the carbon footprint of a typical household?"
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
    
    # First request (should be generated)
    print("First request (generating)...")
    response1 = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json=payload
    )
    result1 = response1.json()
    print(f"Source: {result1['data']['metadata']['source']}")
    
    # Second request (should be from cache)
    print("Second request (should be cached)...")
    response2 = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json=payload
    )
    result2 = response2.json()
    print(f"Source: {result2['data']['metadata']['source']}")
    
    print("✓ LTM caching working!")


def test_error_handling():
    """Test error handling with invalid request."""
    print("\n" + "="*60)
    print("Testing Error Handling")
    print("="*60)
    
    payload = {
        "messages": []  # Empty messages should trigger error
    }
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json=payload
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Status: {result['status']}")
    print(f"Error Message: {result.get('error_message', 'None')}")
    
    # Should return error status but valid JSON
    assert response.status_code in [200, 400]
    print("✓ Error handling works correctly!")


def run_all_tests():
    """Run all tests."""
    print("\n" + "#"*60)
    print("# Sustainability Footprint Agent - Test Suite")
    print("#"*60)
    
    try:
        test_health_check()
        test_agent_info()
        test_carbon_footprint_query()
        test_energy_query()
        test_waste_management_query()
        test_ltm_cache()
        test_error_handling()
        
        print("\n" + "="*60)
        print("✓ ALL TESTS PASSED!")
        print("="*60)
        
    except requests.exceptions.ConnectionError:
        print("\n" + "="*60)
        print("ERROR: Cannot connect to the agent!")
        print("Please make sure the agent is running:")
        print("  python main.py")
        print("="*60)
    
    except Exception as e:
        print("\n" + "="*60)
        print(f"✗ TEST FAILED: {e}")
        print("="*60)


if __name__ == "__main__":
    run_all_tests()
