from graphviz import Digraph

dot = Digraph(
    graph_attr={
        "rankdir": "TB",
        "splines": "ortho",
        "nodesep": "0.8",
        "ranksep": "0.8",
        "bgcolor": "white",
    }
)

box = {
    "shape": "box",
    "style": "filled",
    "fillcolor": "#A8D8D8",
    "color": "#4A9A9A",
    "fontname": "Aporetic Sans",
}
diamond = {
    "shape": "diamond",
    "style": "filled",
    "fillcolor": "#F4CCCC",
    "color": "#C07070",
    "fontname": "Aporetic Sans",
}
start = {
    "shape": "box",
    "style": "filled,rounded",
    "fillcolor": "#FFD966",
    "color": "#C8A000",
    "fontname": "Aporetic Sans",
}

dot.node("start", "Start Game", **start)
dot.node("collision", "Collision?", **diamond)
dot.node("continue", "Continue Game", **box)
dot.node("food", "Food Collision?", **diamond)
dot.node("score", "Score Increases", **box)
dot.node("wall", "Wall Collision?", **diamond)
dot.node("body", "Body Collision", **diamond)
dot.node("finish", "Game Finish\n-> Display Final Score", **box)

# with dot.subgraph() as s:
#     s.attr(rank="same")
#     s.node("collision")
#     s.node("food")
#     s.node("score")

edge_yes = {"color": "#00AA00", "fontname": "Helvetica", "fontsize": "11"}
edge_no = {"color": "#CC0000", "fontname": "Helvetica", "fontsize": "11"}

dot.edge("start", "collision")
dot.edge("collision", "food", label="Yes", **edge_yes)
dot.edge("collision", "continue", label="No", **edge_no)
dot.edge("food", "score", label="Yes", **edge_yes)
dot.edge("food", "wall", label="No", **edge_no)
dot.edge("wall", "finish", label="Yes", **edge_yes)
dot.edge("wall", "body", label="No", **edge_no)
dot.edge("body", "finish", label="Yes", **edge_yes)

dot.render("snake_flowchart", format="png", view=True, cleanup=True)
