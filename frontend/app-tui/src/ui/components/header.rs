use ratatui::layout::Rect;
use:: ratatui::{
    widgets::{Block, Borders, Paragraph},
    Frame,
};

pub fn render_header(frame: &mut Frame, area: Rect) {
        let logo: &str ="
    ░█▀█░█▀█░▀█▀░░░█▀▀░█▀█░█▀▀░█▀▀
    ░█▀█░█▀▀░░█░░░░▀▀█░█▀█░▀▀█░▀▀█
    ░▀░▀░▀░░░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀";
    let header_widget = Paragraph::new(logo).block(Block::default().borders(Borders::BOTTOM));
    frame.render_widget(header_widget, area);
}