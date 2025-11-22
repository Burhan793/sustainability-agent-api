"""
Example usage of the Sustainability Footprint Agent.
Demonstrates how to interact with the agent API.
"""

import requests
import json


def example_basic_query():
    """Example: Simple carbon footprint query."""
    print("\n" + "="*60)
    print("Example 1: Basic Carbon Footprint Query")
    print("="*60)
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "How can I calculate my household carbon footprint?"
                }
            ]
        }
    )
    
    result = response.json()
    print(f"\nQuery: How can I calculate my household carbon footprint?")
    print(f"\nResponse:\n{result['data']['message']}")


def example_conversation():
    """Example: Multi-turn conversation."""
    print("\n" + "="*60)
    print("Example 2: Multi-Turn Conversation")
    print("="*60)
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json={
            "messages": [
                {
                    "role": "assistant",
                    "content": "Hello! I'm your sustainability assistant. How can I help you today?"
                },
                {
                    "role": "user",
                    "content": "I want to reduce my energy consumption."
                },
                {
                    "role": "assistant",
                    "content": "Great goal! What type of building are you looking to optimize?"
                },
                {
                    "role": "user",
                    "content": "A residential home with electric heating."
                }
            ]
        }
    )
    
    result = response.json()
    print(f"\nConversation History: Multi-turn about energy reduction")
    print(f"\nResponse:\n{result['data']['message']}")


def example_specific_calculation():
    """Example: Specific sustainability calculation."""
    print("\n" + "="*60)
    print("Example 3: Specific Calculation Request")
    print("="*60)
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "Calculate the CO2 emissions from a round-trip flight from New York to London."
                }
            ]
        }
    )
    
    result = response.json()
    print(f"\nQuery: Calculate CO2 emissions for NYC-London flight")
    print(f"\nResponse:\n{result['data']['message']}")


def example_recommendations():
    """Example: Get sustainability recommendations."""
    print("\n" + "="*60)
    print("Example 4: Sustainability Recommendations")
    print("="*60)
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "What are the best ways to make my office building more sustainable?"
                }
            ]
        }
    )
    
    result = response.json()
    print(f"\nQuery: Office building sustainability recommendations")
    print(f"\nResponse:\n{result['data']['message']}")


def example_renewable_energy():
    """Example: Renewable energy consultation."""
    print("\n" + "="*60)
    print("Example 5: Renewable Energy Consultation")
    print("="*60)
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "Should I install solar panels on my roof? What are the benefits and ROI?"
                }
            ]
        }
    )
    
    result = response.json()
    print(f"\nQuery: Solar panel installation benefits and ROI")
    print(f"\nResponse:\n{result['data']['message']}")


def example_waste_management():
    """Example: Waste management assessment."""
    print("\n" + "="*60)
    print("Example 6: Waste Management Assessment")
    print("="*60)
    
    response = requests.post(
        "http://localhost:8000/sustainability-footprint-agent",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "How can a small business implement effective waste management and recycling?"
                }
            ]
        }
    )
    
    result = response.json()
    print(f"\nQuery: Small business waste management")
    print(f"\nResponse:\n{result['data']['message']}")


def check_agent_health():
    """Check if agent is running."""
    try:
        response = requests.get("http://localhost:8000/health", timeout=2)
        return response.status_code == 200
    except:
        return False


def main():
    """Run all examples."""
    print("\n" + "#"*60)
    print("# Sustainability Footprint Agent - Usage Examples")
    print("#"*60)
    
    # Check if agent is running
    if not check_agent_health():
        print("\n" + "="*60)
        print("ERROR: Agent is not running!")
        print("Please start the agent first:")
        print("  python main.py")
        print("="*60)
        return
    
    print("\nAgent is running ✓")
    
    try:
        # Run all examples
        example_basic_query()
        input("\nPress Enter to continue to next example...")
        
        example_conversation()
        input("\nPress Enter to continue to next example...")
        
        example_specific_calculation()
        input("\nPress Enter to continue to next example...")
        
        example_recommendations()
        input("\nPress Enter to continue to next example...")
        
        example_renewable_energy()
        input("\nPress Enter to continue to next example...")
        
        example_waste_management()
        
        print("\n" + "="*60)
        print("All examples completed!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\nExamples interrupted by user.")
    except Exception as e:
        print(f"\n\nError running examples: {e}")


if __name__ == "__main__":
    main()
