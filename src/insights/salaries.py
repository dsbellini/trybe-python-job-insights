from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            if job["max_salary"].isdigit():
                if int(job["max_salary"]) > max_salary:
                    max_salary = int(job["max_salary"])
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:
            if job["min_salary"].isdigit():
                if int(job["min_salary"]) < min_salary:
                    min_salary = int(job["min_salary"])
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError(
                "Ambas as chaves 'min_salary' e 'max_salary' são necessárias"
            )

        if not (
            str(job["min_salary"]).isdigit()
            and str(job["max_salary"]).isdigit()
        ):
            raise ValueError(
                "Os valores de 'min_salary' e 'max_salary' devem ser numéricos"
            )

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError(
                "O valor de 'min_salary' não pode ser maior que 'max_salary'"
            )

        if not isinstance(salary, (int, str)):
            raise ValueError("O salário deve ser um número ou string")

        return min_salary <= int(salary) <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        good_salaried_jobs = []

        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    good_salaried_jobs.append(job)
            except (
                ValueError
            ):  # Utiliza os erros do método matches_salary_range
                continue

        return good_salaried_jobs
