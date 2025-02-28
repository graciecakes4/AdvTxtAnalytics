library(shiny)

ui <- fluidPage(
    titlePanel("My First Shiny App"),
    sidebarLayout(
        sidebarPanel(
            sliderInput("num", "Number of Bins:", min = 1, max = 50, value = 30)
        ),
        mainPanel(
            plotOutput("distPlot")
        )
    )
)

server <- function(input, output) {
    output$distPlot <- renderPlot({
        hist(rnorm(500), breaks = input$num, col = "blue", border = "white")
    })
}

shinyApp(ui = ui, server = server)