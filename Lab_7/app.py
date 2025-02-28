from shiny import App, ui, render
import matplotlib.pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.panel_title("My First PyShiny App"),
    ui.input_slider("num", "Number of Bins:", 1, 50, 30),
    ui.output_plot("hist_plot")
)

def server(input, output, session):
    @output
    @render.plot
    def hist_plot():
        data = np.random.randn(500)
        plt.hist(data, bins=input.num(), color="blue", edgecolor="white")

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()