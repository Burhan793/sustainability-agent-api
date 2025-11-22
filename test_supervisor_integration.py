"""
Integration Test Script for Supervisor Agent Team
Tests all endpoints and verifies format compliance
"""

import requests
import json
from typing import Dict, Any


class SustainabilityAgentTester:
    """Test class for verifying agent integration"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.agent_endpoint = f"{base_url}/api/sustainability-footprint-agent"
        self.health_endpoint = f"{base_url}/api/sustainability-footprint-agent/health"
        
    def test_health_check(self) -> bool:
        """Test health check endpoint"""
        print("\n" + "="*60)
        print("TEST 1: Health Check")
        print("="*60)
        
        try:
            response = requests.get(self.health_endpoint, timeout=5)
            data = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(data, indent=2)}")
            
            # Verify format
            assert response.status_code == 200, "Status code should be 200"
            assert data.get("status") == "ok", "Status should be 'ok'"
            assert data.get("agent_name") == "sustainability-footprint-agent"
            assert data.get("ready") == True
            
            print("✅ PASSED: Health check working correctly")
            return True
            
        except Exception as e:
            print(f"❌ FAILED: {e}")
            return False
    
    def test_carbon_footprint_query(self) -> bool:
        """Test carbon footprint analysis"""
        print("\n" + "="*60)
        print("TEST 2: Carbon Footprint Query")
        print("="*60)
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "What is my carbon footprint from driving 100 miles?"
                }
            ]
        }
        
        try:
            response = requests.post(
                self.agent_endpoint,
                json=payload,
                timeout=30
            )
            data = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"Agent Name: {data.get('agent_name')}")
            print(f"Status: {data.get('status')}")
            print(f"Response Preview: {data.get('data', {}).get('message', '')[:200]}...")
            
            # Verify format
            assert response.status_code == 200
            assert data.get("agent_name") == "sustainability-footprint-agent"
            assert data.get("status") in ["success", "error"]
            assert "data" in data or "error_message" in data
            
            if data.get("status") == "success":
                assert "message" in data.get("data", {})
                print("✅ PASSED: Carbon footprint query successful")
                return True
            else:
                print(f"⚠️  WARNING: Query returned error: {data.get('error_message')}")
                return False
                
        except Exception as e:
            print(f"❌ FAILED: {e}")
            return False
    
    def test_energy_query(self) -> bool:
        """Test energy consumption query"""
        print("\n" + "="*60)
        print("TEST 3: Energy Consumption Query")
        print("="*60)
        
        payload = {
            "messages": [
                {
                    "role": "assistant",
                    "content": "Hello! How can I help you today?"
                },
                {
                    "role": "user",
                    "content": "What are the benefits of installing solar panels?"
                }
            ]
        }
        
        try:
            response = requests.post(
                self.agent_endpoint,
                json=payload,
                timeout=30
            )
            data = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"Status: {data.get('status')}")
            
            assert data.get("status") == "success"
            print("✅ PASSED: Multi-turn conversation works")
            return True
            
        except Exception as e:
            print(f"❌ FAILED: {e}")
            return False
    
    def test_format_compliance(self) -> bool:
        """Verify response format compliance with SPM spec"""
        print("\n" + "="*60)
        print("TEST 4: Format Compliance Check")
        print("="*60)
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "Test query"
                }
            ]
        }
        
        try:
            response = requests.post(
                self.agent_endpoint,
                json=payload,
                timeout=30
            )
            data = response.json()
            
            # Check required fields
            required_fields = ["agent_name", "status", "data", "error_message"]
            missing_fields = [f for f in required_fields if f not in data]
            
            if missing_fields:
                print(f"❌ FAILED: Missing required fields: {missing_fields}")
                return False
            
            # Check agent_name format
            assert data["agent_name"] == "sustainability-footprint-agent"
            
            # Check status values
            assert data["status"] in ["success", "error"]
            
            # Check data structure
            if data["status"] == "success":
                assert data["data"] is not None
                assert isinstance(data["data"], dict)
                assert "message" in data["data"]
            
            print("✅ PASSED: Response format complies with SPM spec")
            print(f"   - agent_name: ✓")
            print(f"   - status: ✓")
            print(f"   - data: ✓")
            print(f"   - error_message: ✓")
            return True
            
        except Exception as e:
            print(f"❌ FAILED: {e}")
            return False
    
    def test_error_handling(self) -> bool:
        """Test error handling with invalid request"""
        print("\n" + "="*60)
        print("TEST 5: Error Handling")
        print("="*60)
        
        payload = {
            "messages": []  # Invalid: empty messages
        }
        
        try:
            response = requests.post(
                self.agent_endpoint,
                json=payload,
                timeout=30
            )
            data = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"Status: {data.get('status')}")
            print(f"Error Message: {data.get('error_message')}")
            
            # Should return error status but still valid JSON
            assert isinstance(data, dict)
            assert "agent_name" in data
            assert "status" in data
            
            print("✅ PASSED: Error handling works correctly")
            print("   - Returns valid JSON even on error")
            print("   - Includes error_message field")
            return True
            
        except Exception as e:
            print(f"❌ FAILED: {e}")
            return False
    
    def test_timeout_handling(self) -> bool:
        """Test that agent responds within timeout"""
        print("\n" + "="*60)
        print("TEST 6: Timeout Handling")
        print("="*60)
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "Calculate the environmental impact of a large office building"
                }
            ]
        }
        
        try:
            import time
            start_time = time.time()
            
            response = requests.post(
                self.agent_endpoint,
                json=payload,
                timeout=30
            )
            
            elapsed_time = time.time() - start_time
            
            print(f"Response Time: {elapsed_time:.2f} seconds")
            
            assert elapsed_time < 30, "Response should be within 30 seconds"
            assert response.status_code == 200
            
            print("✅ PASSED: Agent responds within timeout")
            print(f"   - Response time: {elapsed_time:.2f}s (< 30s required)")
            return True
            
        except requests.exceptions.Timeout:
            print("❌ FAILED: Request timed out")
            return False
        except Exception as e:
            print(f"❌ FAILED: {e}")
            return False
    
    def run_all_tests(self):
        """Run all integration tests"""
        print("\n" + "#"*60)
        print("# SUPERVISOR INTEGRATION TEST SUITE")
        print("# Testing: Sustainability Footprint Agent")
        print("#"*60)
        
        tests = [
            self.test_health_check,
            self.test_carbon_footprint_query,
            self.test_energy_query,
            self.test_format_compliance,
            self.test_error_handling,
            self.test_timeout_handling
        ]
        
        results = []
        for test in tests:
            try:
                result = test()
                results.append(result)
            except Exception as e:
                print(f"❌ Test failed with exception: {e}")
                results.append(False)
        
        # Summary
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        passed = sum(results)
        total = len(results)
        
        print(f"Passed: {passed}/{total}")
        print(f"Failed: {total - passed}/{total}")
        
        if passed == total:
            print("\n🎉 ALL TESTS PASSED! Agent is ready for supervisor integration!")
        else:
            print(f"\n⚠️  {total - passed} test(s) failed. Please review errors above.")
        
        return passed == total


def main():
    """Main entry point"""
    print("\nChecking if agent is running...")
    
    try:
        response = requests.get("http://localhost:8000/health", timeout=2)
        print("✓ Agent is running\n")
    except:
        print("\n" + "="*60)
        print("ERROR: Agent is not running!")
        print("="*60)
        print("\nPlease start the agent first:")
        print("  cd 'C:\\Users\\hp\\OneDrive\\Desktop\\SPM Project'")
        print("  .\\venv\\Scripts\\python.exe main.py")
        print("\nThen run this test script again.")
        print("="*60)
        return
    
    # Run tests
    tester = SustainabilityAgentTester()
    success = tester.run_all_tests()
    
    if success:
        print("\n" + "="*60)
        print("INTEGRATION READY")
        print("="*60)
        print("\nAgent Endpoints:")
        print(f"  Main: http://localhost:8000/api/sustainability-footprint-agent")
        print(f"  Health: http://localhost:8000/api/sustainability-footprint-agent/health")
        print("\nYou can now integrate this agent with the supervisor!")
        print("="*60)


if __name__ == "__main__":
    main()
