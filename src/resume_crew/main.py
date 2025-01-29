#!/usr/bin/env python
import sys
import warnings
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        'job_url': 'https://www.linkedin.com/jobs/search/?currentJobId=4119856777&keywords=software%20engineer&location=sydney%20nsw&originalSubdomain=au',
        'company_name': 'Dovetail'
    }
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
