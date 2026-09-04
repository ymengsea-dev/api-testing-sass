// this is where keyboard and terminal event handle 
use crate::controller::app_state::{AppState, InputMode};
use crossterm::event::{self, Event, KeyCode, KeyEventKind};
use std::io;

pub fn handle_key_events(state: &mut AppState) -> io::Result<()> {
    if let Event::Key(key) = event::read()? {
        if key.kind == KeyEventKind::Press {
            match state.input_mode {
                InputMode::Normal => match key.code {
                    KeyCode::Char('q') => state.quit(),
                    KeyCode::Char('i') => state.input_mode = InputMode::Typing,
                    KeyCode::Down => state.next(),
                    KeyCode::Up=> state.prev(),
                    _ => {}
                },
                InputMode::Typing => match key.code {
                    KeyCode::Esc => {
                        state.input_mode = InputMode::Normal;
                        state.input.clear();
                    }, // press escape -> return to use nav mode
                    KeyCode::Left => state.move_cursor_left(),
                    KeyCode::Right => state.move_cursor_right(),
                    KeyCode::Char(c) => state.enter_char(c),
                    KeyCode::Backspace => state.delete_char(),
                    KeyCode::Enter => {
                        state.input.clear();
                        state.cursor_position = 0;
                        state.input_mode = InputMode::Normal;
                    }
                    _ => {}
                },
            }

        }
    }
    Ok(())
}