use ratatui::layout::Rect;
use:: ratatui::{
    widgets::{Block, Borders, Paragraph},
    Frame,
};

pub fn render_footer(frame: &mut Frame, area: Rect ){
    let footer_widget = Paragraph::new("    Input prompt ...").block(Block::default().borders(Borders::TOP));
    frame.render_widget(footer_widget, area);
}