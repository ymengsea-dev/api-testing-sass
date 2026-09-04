use ratatui::{
    layout::Rect,
    widgets::{Block, Paragraph},
    Frame,
};

pub fn render_history_view(frame: &mut Frame, area: Rect){
    let label = Paragraph::new("history")
    .block(Block::default());
    frame.render_widget(label, area);
}