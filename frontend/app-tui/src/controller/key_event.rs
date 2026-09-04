// this is where keyboard and terminal event handle 
use crate::controller::app_state::AppState;
use crossterm::event::{self, Event, KeyCode, KeyEventKind};
use std::io;

pub fn handle_key_events(state: &mut AppState) -> io::Result<()> {
    if let Event::Key(key) = event::read()? {
        if key.kind == KeyEventKind::Press {
            match key.code {
                KeyCode::Char('q') => state.quit(),
                KeyCode::Down | KeyCode::Char('j') => state.next(),
                KeyCode::Up | KeyCode::Char('k') => state.prev(),
                _ => {}
            }
        }
    }
    Ok(())
}