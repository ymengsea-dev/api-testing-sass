use ratatui::{
    layout::Rect,
    Frame,
};

use crate::ui::screens::{
    render_help_view,
    render_endpoints_view,
    render_test_cases_view,
    render_history_view,
    render_environment_view};


/// Dynamic Detail View Component
pub fn render_detail(frame: &mut Frame, area: Rect, selected_index: usize){
    match  selected_index {
        0 => render_endpoints_view(frame, area),
        1 => render_test_cases_view(frame, area),
        2 => render_history_view(frame, area),
        3 => render_environment_view(frame, area),
        4 => render_help_view(frame, area),
        _ => render_help_view(frame, area),
    }
}
