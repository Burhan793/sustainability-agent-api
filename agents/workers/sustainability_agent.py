"""
Sustainability Footprint Worker Agent.
Analyzes carbon footprint, energy consumption, and environmental impact.
"""

import sys
import os
from typing import Any, Optional, Dict
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.worker_base import AbstractWorkerAgent
from shared.ltm_storage import LTMStorage
from openai import OpenAI


class SustainabilityFootprintAgent(AbstractWorkerAgent):
    """
    Worker agent specialized in sustainability and environmental footprint analysis.
    Provides insights on carbon footprint, energy consumption, waste management, etc.
    """
    
    def __init__(
        self, 
        agent_id: str = "sustainability-footprint-agent",
        supervisor_id: str = "supervisor-agent",
        openai_api_key: Optional[str] = None
    ):
        super().__init__(agent_id, supervisor_id)
        
        # Initialize LTM storage
        ltm_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "shared", "LTM", "sustainability-footprint-agent"
        )
        self.ltm = LTMStorage(ltm_path)
        
        # Initialize OpenAI client
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None
            print(f"[{self._id}] Warning: No OpenAI API key provided. Using rule-based responses.")
        
        # System prompt for sustainability analysis
        self.system_prompt = """You are a Sustainability Footprint Agent, an expert AI assistant specializing in environmental impact analysis, carbon footprint calculations, energy efficiency, waste management, and sustainability metrics.

Your expertise includes:
- Carbon footprint analysis and CO2 emissions calculation
- Energy consumption tracking and optimization
- Waste management assessment and reduction strategies
- Renewable energy recommendations
- Green building certifications and sustainable practices
- Environmental impact analysis
- Sustainability reporting and metrics

Provide accurate, actionable insights with specific recommendations. When providing carbon calculations, use standard emission factors. Always consider both immediate and long-term environmental impacts.

Keep responses concise but informative, focusing on practical sustainability solutions."""
    
    def process_task(self, task_data: dict) -> dict:
        """
        Process sustainability-related queries.
        
        Args:
            task_data: Dictionary containing the query and parameters
            
        Returns:
            Dictionary with analysis results
        """
        query = task_data.get("query", "")
        messages = task_data.get("messages", [])
        
        if not query and messages:
            # Extract query from messages
            user_messages = [msg for msg in messages if msg.get("role") == "user"]
            if user_messages:
                query = user_messages[-1].get("content", "")
        
        if not query:
            raise ValueError("No query provided in task data")
        
        # LTM caching disabled - always generate fresh responses
        # cached_response = self.ltm.search_similar(query)
        # if cached_response:
        #     print(f"[{self._id}] Found cached response in LTM")
        #     return {
        #         "message": cached_response,
        #         "source": "ltm_cache",
        #         "query": query
        #     }
        
        # Generate new response
        response = self._generate_sustainability_analysis(query, messages)
        
        # Store successful response in LTM (optional - currently disabled)
        # self.ltm.store_response(query, response)
        
        return {
            "message": response,
            "source": "generated",
            "query": query
        }
    
    def _generate_sustainability_analysis(self, query: str, messages: list = None) -> str:
        """
        Generate sustainability analysis using OpenAI or rule-based approach.
        
        Args:
            query: User query
            messages: Conversation history
            
        Returns:
            Analysis response
        """
        if self.client:
            try:
                # Prepare messages for OpenAI
                conversation = [{"role": "system", "content": self.system_prompt}]
                
                if messages:
                    for msg in messages:
                        conversation.append({
                            "role": msg.get("role", "user"),
                            "content": msg.get("content", "")
                        })
                else:
                    conversation.append({"role": "user", "content": query})
                
                # Call OpenAI API
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=conversation,
                    temperature=0.7,
                    max_tokens=500
                )
                
                return response.choices[0].message.content
            
            except Exception as e:
                print(f"[{self._id}] Error calling OpenAI: {e}")
                return self._rule_based_response(query)
        else:
            return self._rule_based_response(query)
    
    def _rule_based_response(self, query: str) -> str:
        """
        Fallback rule-based response when OpenAI is not available.
        
        Args:
            query: User query
            
        Returns:
            Rule-based response
        """
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["carbon", "footprint", "co2", "emissions"]):
            return """Carbon footprint analysis involves measuring total greenhouse gas emissions. Key factors include:

1. Transportation: Vehicle emissions, flight miles
2. Energy consumption: Electricity, heating, cooling
3. Food choices: Meat vs. plant-based diets
4. Waste generation: Recycling rates, landfill impact

Average individual carbon footprint is ~4 tons CO2/year. Reduction strategies:
- Use public transport or electric vehicles
- Switch to renewable energy
- Reduce meat consumption
- Improve home insulation"""
        
        elif any(word in query_lower for word in ["energy", "consumption", "electricity"]):
            return """Energy consumption analysis focuses on efficiency and renewable sources:

1. Audit current usage: Identify high-consumption appliances
2. Energy efficiency: LED bulbs, Energy Star appliances
3. Renewable energy: Solar panels, wind power options
4. Smart systems: Thermostats, automated lighting

Typical household uses 10,000 kWh/year. Reduction tips:
- Upgrade to efficient appliances
- Install programmable thermostats
- Consider solar installation
- Improve insulation and sealing"""
        
        elif any(word in query_lower for word in ["waste", "recycling", "trash"]):
            return """Waste management assessment evaluates reduction and recycling:

1. Waste audit: Track types and amounts
2. Recycling: Proper sorting and contamination prevention
3. Composting: Organic waste reduction
4. Reduction: Minimize single-use items

Average person generates 4.5 lbs waste/day. Best practices:
- Implement comprehensive recycling
- Start composting organic waste
- Choose reusable over disposable
- Support circular economy products"""
        
        elif any(word in query_lower for word in ["renewable", "solar", "wind"]):
            return """Renewable energy recommendations for sustainability:

1. Solar power: Rooftop panels, community solar
2. Wind energy: Small turbines, utility programs
3. Geothermal: Heat pumps for heating/cooling
4. Hydroelectric: Micro-hydro for suitable locations

Benefits:
- Reduce carbon emissions by 80%+
- Long-term cost savings
- Energy independence
- Increase property value

Start with energy audit to determine best options."""
        
        else:
            return """As a Sustainability Footprint Agent, I can help you with:

1. Carbon footprint analysis and reduction strategies
2. Energy consumption tracking and optimization
3. Waste management and recycling programs
4. Renewable energy recommendations
5. Green building certifications
6. Environmental impact assessments
7. Sustainability metrics and reporting

Please provide more specific details about your sustainability concerns, and I'll provide targeted analysis and recommendations."""
    
    def send_message(self, recipient: str, message_obj: dict):
        """
        Send message to supervisor (implementation for completeness).
        In API mode, this is handled by the FastAPI layer.
        """
        print(f"[{self._id}] Sending message to {recipient}: {json.dumps(message_obj, indent=2)}")
    
    def write_to_ltm(self, key: str, value: Any) -> bool:
        """Write to Long-Term Memory."""
        return self.ltm.write(key, value)
    
    def read_from_ltm(self, key: str) -> Optional[Any]:
        """Read from Long-Term Memory."""
        return self.ltm.read(key)
    
    def process_api_request(self, messages: list) -> Dict[str, Any]:
        """
        Process API request from FastAPI endpoint.
        
        Args:
            messages: List of message dictionaries
            
        Returns:
            Response dictionary
        """
        try:
            # Extract user query
            user_messages = [msg for msg in messages if msg.get("role") == "user"]
            if not user_messages:
                raise ValueError("No user message found in request")
            
            query = user_messages[-1].get("content", "")
            
            # Process through standard task processing
            task_data = {
                "query": query,
                "messages": messages
            }
            
            result = self.process_task(task_data)
            
            return {
                "message": result.get("message", ""),
                "metadata": {
                    "source": result.get("source", "unknown"),
                    "query": query
                }
            }
        
        except Exception as e:
            raise Exception(f"Error processing request: {str(e)}")
