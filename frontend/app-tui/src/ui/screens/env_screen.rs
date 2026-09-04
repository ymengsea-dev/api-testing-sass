use ratatui::{
    layout::Rect,
    widgets::{Block, Paragraph},
    Frame,
};

pub fn render_environment_view(frame: &mut Frame, area: Rect){
    let label = Paragraph::new("environment")
    .block(Block::default());
    frame.render_widget(label, area);
}