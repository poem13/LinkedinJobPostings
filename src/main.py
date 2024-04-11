import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


def fetch_joblocations():
    df = pd.read_csv('C:/Users/poemy/IdeaProjects/LinkedinDataPostings/data/postings.csv')
    locations = df['job_location'].values.tolist()
    US = "United States"
    while US in locations:
        locations.remove(US)
    return locations


def fetch_joblevels():
    df = pd.read_csv('C:/Users/poemy/IdeaProjects/LinkedinDataPostings/data/postings.csv')
    levels = df['job level'].values.tolist()
    return levels


def fetch_jobtype():
    df = pd.read_csv('C:/Users/poemy/IdeaProjects/LinkedinDataPostings/data/postings.csv')
    types = df['job_type'].values.tolist()
    return types


def fetch_jobskills():
    df = pd.read_csv('C:/Users/poemy/IdeaProjects/LinkedinDataPostings/data/postings.csv')
    skills = df['job_skills'].str.split(', ').explode('job_skills')
    #return skills.values.tolist()
    return skills.value_counts()


def graph_bar(fetch_function, title, ylabel, xlabel, is_rotate):
    freq = Counter(fetch_function).most_common(10)
    xdata = [xdata for xdata, _ in freq]
    ydata = [ydata for _, ydata in freq]
    plt.bar(xdata, ydata, color=color)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    if is_rotate:
        plt.xticks(rotation=30, fontsize='small')
    plt.show()


if __name__ == '__main__':
    plt.rcParams["font.family"] = "Arial"
    color = ['rosybrown', 'lightcoral', 'indianred', 'brown', 'maroon']
    ylabel = "Frequency"

    graph_bar(fetch_joblocations(), "Most common data job locations", ylabel, "Cities", True)
    graph_bar(fetch_joblevels(), "Most common job levels in Data jobs", ylabel, "Job Levels", False)
    graph_bar(fetch_jobtype(), "Most common job types in Data jobs", ylabel, "Job Types", False)

    plt.figure(figsize=(15, 80))
    plt.xlabel("Frequency")
    plt.ylabel("Skills")
    plt.title("Top 100 skills for data jobs")
    plt.yticks(rotation=50, fontsize='small')
    fetch_jobskills()[:100].sort_values().plot(kind='barh', color=color)
    plt.show()
