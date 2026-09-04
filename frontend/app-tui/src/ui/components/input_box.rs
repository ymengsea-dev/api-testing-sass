use crate::controller::app_state::{AppState, InputMode};
use:: ratatui::{
    layout::Rect,
    style::{Color,Style},
    widgets::{Block, Borders, Paragraph},
    Frame,
};

pub fn render_input_box(frame: &mut Frame, area: Rect, state: &AppState ){

    let (_border_color, placeholder) = match &state.input_mode {
        InputMode::Normal => (Color::Gray, "    Input (Press 'i' to type) "),
        InputMode::Typing => (Color::Gray, "❱    Editing Command (Press Ese return to nav mode)"),
    };

    let contnent = if state.input.is_empty(){
        placeholder.to_string()
    }else {
       format!(" {}", state.input.as_str()) 
    };

    let input_box_widget = Paragraph::new(contnent)
        .style(Style::default())
        .block(
            Block::default()
                .borders(Borders::TOP)
        );
    
    frame.render_widget(input_box_widget, area);
    
    // show cursor when in input mode
    if let InputMode::Typing = &state.input_mode {
        frame.set_cursor_position((
            area.x + 1 + state.cursor_position as u16,
            area.y + 1,
        ));
    }
}