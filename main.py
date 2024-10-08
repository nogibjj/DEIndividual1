"""
Main cli or app entry point
"""

from mylib.lib import (
    load_and_preprocess,
    process_mean,
    process_quantile,
    process_median,
    process_std,
    NBA_bar_mp,
    NBA_histogram_poss
)


def general_describe(csv):
    """general describe"""
    general_df = load_and_preprocess(csv)
    return general_df.describe()


def custom_describe(csv, col):
    """custom describe"""
    general_df = load_and_preprocess(csv)
    describe_dict = {
        "name": col,
        "mean": process_mean(general_df, col),
        "std": process_std(general_df, col),
        "median": process_median(general_df, col),
        "25 quantile": process_quantile(general_df, col, 0.25),
    }
    return describe_dict


def general_viz_combined(general_df, jupyter_render):
    """saves all the figures at once"""
    NBA_bar_mp(general_df, jupyter_render)
    NBA_histogram_poss(general_df, jupyter_render)



def save_to_markdown(csv):
    """save summary report to markdown"""
    general_df = load_and_preprocess(csv)
    describe_df = general_describe(csv)
    markdown_table1 = describe_df.to_markdown()
    general_viz_combined(general_df, False)
    # Write the markdown table to a file
    with open("nba_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](nba_mp.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz2](nba_poss.png)\n")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    # add_cli()
    csv = "https://projects.fivethirtyeight.com/nba-model/2023/latest_RAPTOR_by_player.csv"
    general_df = load_and_preprocess(csv)
    custom_describe(csv, "mp")
    general_viz_combined(general_df, True)
    save_to_markdown(csv)
    # print(df)
    # print(process_mean(df, 'mp'))
    # NBA_histogram_poss(df, jupyter_render)
