use ratatui::{
     layout::{Constraint, Direction, Layout, Rect},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, List, ListItem, Paragraph},
    Frame,
};

// color style helper
fn help_item<'a>(command: &'a str, description: &'a str) -> ListItem<'a> {
    ListItem::new(Line::from(vec![
        Span::styled(
            format!("       {:<28}", command),
            Style::default()
                .fg(Color::Cyan)
                .add_modifier(Modifier::BOLD),
        ),
        Span::raw(description),
    ]))
}

// rander view
pub fn render_help_view(frame: &mut Frame, area: Rect) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(2),
            Constraint::Min(0),
        ])
        .split(area);

    let label = Paragraph::new("    Help & Keyboard Shortcuts")
        .block(Block::default());

    let items = vec![
        help_item(
            "/execute <endpoint-name>",
            "Run HTTP request for the configured endpoint",
        ),
        help_item("/new-endpoint", "Add a new curl endpoint for testing"),
        help_item(
            "/recent-executed",
            "Show the most recently executed endpoint",
        ),
        help_item(
            "/test-library",
            "Show pre-built and custom test cases",
        ),
        help_item("/history", "Show execution history"),
        help_item(
            "/clear-history",
            "Clear endpoint execution history",
        ),
        help_item("↓", "Move down in sidebar menu"),
        help_item("↑", "Move up in sidebar menu"),
        help_item("q", "Exit application"),
    ];

    let help_items = List::new(items)
        .block(Block::default());

    frame.render_widget(label, chunks[0]);
    frame.render_widget(help_items, chunks[1]);
}