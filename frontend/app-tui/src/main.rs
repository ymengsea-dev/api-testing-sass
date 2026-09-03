use std::io;
use crossterm::event::{self, Event, KeyCode};
use ratatui::{
    DefaultTerminal,
    Frame,
    widgets::{Block, Borders, Paragraph},
};

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
    loop {
        // change what displayed in the terminal 
        terminal.draw(draw)?;
        
        // if the event ket = q break the loop end the app
        if let Event::Key(key) = event::read()? {
            if key.code == KeyCode::Char('q'){
                return Ok(());
            }
        }
    }
}

// frame represent the current terminal screen
// @mut Frame mean borrow the frame and allow this func to modify it 
fn draw(frame: &mut Frame){

    // create block
    // blcok is ratatui widget use as containter
    let block = Block::default()
        .title(" API Scenario Tester ") // this add title to the block 
        .borders(Borders::ALL); // // add border 

    // create a paragraph block
    // .block(blcok) tell ratatui to use the created block as container
    let paragraph = Paragraph::new("Welcome to API Scenario Tester\n\nPress q to quit.")
        .block(block);
    
    // this render the widget , this case the paragraph that wrap with container
    // frame.area(): return entire availabel  area, ex: terminal is 80col x 24 row. 
    // area will return x=0, y=0, width = 80, height = 24 
    frame.render_widget(paragraph, frame.area());
}
