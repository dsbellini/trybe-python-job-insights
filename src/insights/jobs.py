from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        self.jobs_list = list()

        with open(path, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                self.jobs_list.append(dict(row))
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = []
        for job in self.jobs_list:
            job_types.append(job["job_type"])
        return list(set(job_types))

    def filter_by_multiple_criteria(
        self, jobs: List[dict], filter_criteria: dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("O filtro deve ser um dicionário")

        filtered_jobs = jobs.copy()
        for key, value in filter_criteria.items():
            filtered_jobs = [
                job for job in filtered_jobs if job.get(key) == value
            ]

        return filtered_jobs
