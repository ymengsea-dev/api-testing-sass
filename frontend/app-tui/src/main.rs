use std::io;
use crossterm::event::{self, Event, KeyCode};
use ratatui::{
    layout::{Constraint, Direction, Layout},
    DefaultTerminal,
    Frame,
    widgets::{Block, Borders, Paragraph},
};

struct App {
    selected: usize,
}

//  program entry point
//  main return result
// io::Result<()> is shorthand of Result<(), std::io::Error>
// io is rust standard lib for input/output etc
fn main() -> io::Result<()> {

    //  initialize the terminal and it mutable because it will be alot of state change
    let mut terminal = ratatui::init();

    // this run the application
    // &     = borrow
    // mut   = allow modification
    let result = run(&mut terminal);
    
    // while ratatui running terminal maybe in special state (TUI mode)
    // so after TUIi finished, ratatui restore it back to normal (normal terminal)
    ratatui::restore();

    return result;
}

// the main event loop for ratatui app
fn run(terminal: &mut DefaultTerminal) -> io::Result<()>{

    let mut app = App {
        selected: 0,
    };

    loop {
        // change what displayed in the terminal 
        terminal.draw(|frame| draw(frame, &app))?;
        
        // if the event ket = q break the loop end the app
        if let Event::Key(key) = event::read()? {
            match key.code {

                KeyCode::Char('q') => {
                    return Ok(());
                }

                KeyCode::Down => {
                    if app.selected < 2 {
                        app.selected += 1;
                    }
                }

                KeyCode::Up => {
                    if app.selected > 0 {
                        app.selected -= 1;
                    }
                }

                // this mean anything else do nothing
                // _ is called wildcard pattern
                _=> {} 
            }
        }
    };
}

// frame represent the current terminal screen
// @mut Frame mean borrow the frame and allow this func to modify it 
fn draw(frame: &mut Frame, app: &App){

    let outer_block = Block::default()
        .borders(Borders::ALL);

    let inner_area = outer_block.inner(frame.area());

    frame.render_widget(outer_block, frame.area());

    let logo: &str = "
    ░█▀█░█▀█░▀█▀░░░█▀▀░█▀█░█▀▀░█▀▀
    ░█▀█░█▀▀░░█░░░░▀▀█░█▀█░▀▀█░▀▀█
    ░▀░▀░▀░░░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀";

    let items = ["Endpoints", "Scenarios", "Environment"];

    let main_layout = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(7),
            Constraint:: Min(1),
            Constraint::Length(3),
        ])
        .split(inner_area);

    let header = Paragraph::new(logo)
        .block(
            Block::default()
            .borders(Borders::BOTTOM)
        );

    let footer = Paragraph::new("[↑↓] Navigate     [q] Quit")
        .block(
            Block::default()
                .borders(Borders::TOP)
        );

    let content_layout = Layout::default()
        .direction(Direction::Horizontal)
            .constraints([
                Constraint::Percentage(30),
                Constraint::Percentage(70),
            ])
            .split(main_layout[1]);
    
    let mut sidebar_content = String:: new();

    // we iterate throught menus
    // the .enumerate also give us index without it we got only item, ex: "Endpoints"
    // with it we got : index = 0, item = "Endpoints"
    for (index, item) in items.iter().enumerate(){
        if index == app.selected {
            sidebar_content.push_str(&format!("➜    {}\n", item));
        } else {
            sidebar_content.push_str(&format!("     {}\n", item));
        }
    }
    
    let sidebar = Paragraph::new(sidebar_content)
        .block(
            Block::default()
                .borders(Borders::RIGHT)
        );
    
    let detail = Paragraph::new("Detail")
        .block(
            Block::default()
        );
    
    frame.render_widget(sidebar, content_layout[0]);
    frame.render_widget(detail, content_layout[1]);
    frame.render_widget(header, main_layout[0]);
    frame.render_widget(footer, main_layout[2]);
}
