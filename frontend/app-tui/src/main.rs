mod api;
mod controller;
mod exception;
mod models;
mod ui;

use controller::{handle_key_events, AppState};
use std::io;
use ui::render;

//  program entry point
//  main return result
// io::Result<()> is shorthand of Result<(), std::io::Error>
// io is rust standard lib for input/output etc
fn main() -> io::Result<()> {

    let mut terminal = ratatui::init();
    let mut state = AppState::new();

    while !state.should_quit {
        terminal.draw(|frame| render(frame, &state))?;
        handle_key_events(&mut state)?;
    }

    ratatui::restore();
    Ok(())
}
