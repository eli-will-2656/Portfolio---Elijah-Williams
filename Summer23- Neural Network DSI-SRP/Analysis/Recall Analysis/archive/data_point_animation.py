import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np; np.random.seed(1)

def main():
    # (0) Load in Data
    df = pd.read_csv("C:\Summer 2023 - DSI-SRP\My Analysis\idea_units_arous_and_valence.csv")
    item_strings = df["item_string"].to_list()
    rec_prob = df["recall"].to_list()
    emot_power = df["emotional_power"].to_list()
    passage = df["passage"].to_list()

    # (1) Plot points 

    plot_annotated_data_points(x=emot_power, 
                           y=rec_prob,
                           names=item_strings, 
                           c=passage,    # Assign a color based on passages
                           title="Emotional Power vs Memorability of Idea Units",
                           xlabel="Emotional Power of Word in Idea Unit",
                           ylabel="Probability of Recall",
                           )

def plot_annotated_data_points(x, y, names, c, title="", xlabel="", ylabel=""):
    """Plot annotated data points analysis.

    Args:
        x (List[int]): x-coordinates
        y (List[int]): y-coordinates
        names (List[str]): text for each data pint
        c (List[int]): color assignment for data point 
        title (str): title
        xlabel: x-axis label
        ylabel: y-axis label
    """

    # (2) Customize Scatter Plot
    norm = plt.Normalize(vmin=min(c),vmax=max(c))  # Way to linearly scale color data into a [0-1] range 
    cmap = mpl.colormaps['viridis']  # Color map associates each number in [0,1] with a color
    fig, ax = plt.subplots()   
    sc = plt.scatter(x,y,c=c,s=50, cmap=cmap, norm=norm, alpha=0.8) # creating a scatter plot

    # 
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
 
    annot = ax.annotate(text="", xy=(0,0), xytext=(20,20), # Labels points with a text
                        textcoords="offset points",    # Specifices coordinates of text 
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    
    annot.set_visible(False)    # start off with label as invisible

    def update_annot(ind):  # helper function that runs whenever datapoint is clicked on 
        index = ind["ind"][0]               # index of data point
        pos = sc.get_offsets()[index]       # x,y position of data point
        annot.xy = pos

        text = names[index]          # Text of the annotation

        annot.set_fontsize("x-small")
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor(cmap(norm(c[index])))
        annot.get_bbox_patch().set_alpha(0.4)
        

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.show()
    
if __name__ == "__main__":   
    main()