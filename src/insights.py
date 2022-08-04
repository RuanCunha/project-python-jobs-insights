from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    result = set()
    for job in jobs_list:
        result.add(job["job_type"])
    return result


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    result = [job for job in jobs if job["job_type"] == job_type]
    return result


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    result = set()
    for job in jobs_list:
        if job["industry"] != "":
            result.add(job["industry"])
    return result


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    result = [job for job in jobs if job["industry"] == industry]
    return result


def checkIfDigit(list, min_or_max):
    result = list[0][min_or_max]
    count = 0
    while result.isdigit() is False:
        count += 1
        result = list[count][min_or_max]
        if count > 10:
            break
    return result


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    result = checkIfDigit(jobs_list, "max_salary")

    result = int(result)
    for job in jobs_list:
        if job["max_salary"].isdigit():
            if int(job["max_salary"]) > result:
                result = int(job["max_salary"])
    return result


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    result = checkIfDigit(jobs_list, "min_salary")

    result = int(result)
    for job in jobs_list:
        if job["min_salary"].isdigit():
            if int(job["min_salary"]) < result:
                result = int(job["min_salary"])
    return result


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        if int(job["max_salary"]) < int(job["min_salary"]):
            raise ValueError('Valor invalido')

        return int(job["min_salary"]) <= salary <= int(job["max_salary"])
    except KeyError:
        raise ValueError('Min e/ou Max Salary não existe')
    except TypeError:
        raise ValueError('Valor invalido')


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                print(job)
                result.append(job)
        except ValueError:
            pass
    return result
