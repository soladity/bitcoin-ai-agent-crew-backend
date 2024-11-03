from fastapi import APIRouter, HTTPException, Body, Depends
from services.crew_services import execute_crew
from tools.tools_factory import initialize_tools
from .verify_profile import verify_profile

router = APIRouter()


@router.post("/execute_crew/{crew_id}")
async def execute_crew_endpoint(
    crew_id: int,
    input_str: str = Body(...),
    account_index: int = Depends(verify_profile),
):
    try:
        # Execute the crew logic with the provided input string
        result = execute_crew(str(account_index), crew_id, input_str)

        return {"result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {str(e)}")


@router.get("/tools")
async def get_avaliable_tools():
    try:
        tools_map = initialize_tools("0")
        response = {
            tool_name: tool_instance.description
            for tool_name, tool_instance in tools_map.items()
        }

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {str(e)}")
