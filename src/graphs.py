"""Graph generator."""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def city_general_graph(city_table_path):
    """Plot the general status of infections with respect to city."""
    city_general = pd.read_csv(city_table_path)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(13, 5))
    sns.barplot(
        x="City",
        y="Infection Count",
        data=city_general,
        color=(0.2, 0.4, 0.6, 0.6),
    )
    plt.savefig(os.path.splitext(city_table_path)[0], dpi=300)


def mask_graph(mask_table_path):
    """Plot the status of infections with respect to mask policy."""
    mask_policy = pd.read_csv(mask_table_path)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.barplot(
        x="Mask Policy",
        y="Infection Count",
        data=mask_policy,
        color=(0.2, 0.4, 0.6, 0.6),
    )
    plt.savefig(os.path.splitext(mask_table_path)[0], dpi=300)


def cap_graph(cap_table_path):
    """Plot the status of infections with respect to capacity policy."""
    max_cap = pd.read_csv(cap_table_path)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(9, 5))
    sns.barplot(
        x="Maximum Capacity",
        y="Infection Count",
        data=max_cap,
        color=(0.2, 0.4, 0.6, 0.6),
    )
    plt.savefig(os.path.splitext(cap_table_path)[0], dpi=300)
