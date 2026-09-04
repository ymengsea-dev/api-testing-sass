use ratatui::{
    layout::Rect,
    widgets::{Block, Paragraph},
    Frame,
};


pub fn render_endpoints_view(frame: &mut Frame, area: Rect){
    let label = Paragraph::new("endpoint vide")
    .block(Block::default());
    frame.render_widget(label, area);
}
