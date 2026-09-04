use ratatui::{
    layout::Rect,
    widgets::{Block, Paragraph},
    Frame,
};
pub fn render_test_cases_view(frame: &mut Frame, area: Rect){
    let label = Paragraph::new("test cases")
    .block(Block::default());
    frame.render_widget(label, area);
}
