use crate::controller::AppState;
use crate::ui::components::{render_footer, render_header, render_detail};
use:: ratatui::{
    layout::{Constraint, Direction, Layout},
    style::{Color, Style},
    widgets::{Block, Borders, List, ListItem, Paragraph},
    Frame,
};

pub fn render(frame: &mut Frame, state: &AppState){
    let outer_block = Block::default().borders(Borders::ALL);
    let inner_area = outer_block.inner(frame.area());
    frame.render_widget(outer_block, frame.area());

    let main_layout = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(5),
            Constraint::Min(1),
            Constraint::Length(3),
        ])
        .split(inner_area);

    // header
    render_header(frame, main_layout[0]);

    // footer
    render_footer(frame, main_layout[2]);

    // body content split
    let content_layout = Layout::default()
        .direction(Direction::Horizontal)
            .constraints([
                Constraint::Percentage(25),
                Constraint::Percentage(75),
            ])
            .split(main_layout[1]);

    let sidebar_layout = Layout::default()
        .direction(Direction::Vertical)
            .constraints([
                Constraint::Percentage(80),
                Constraint::Percentage(20)
            ])
            .split(content_layout[0]);
    
    // selected menu in sidebar
    let list_items: Vec<ListItem> = state
        .items
        .iter()
        .enumerate()
        .map(|(i, item)| {
            if i == state.selected {
                ListItem::new(format!("➜   {}", item)).style(Style::default().fg(Color::Cyan).bold())
            } else {
                ListItem::new(format!("    {}", item)).style(Style::default().fg(Color::DarkGray))
            }
        })
        .collect();

    // sidebar
    // sidebar menu list 
    let sidebar_menu = List::new(list_items)
        .block(Block::default().borders(Borders::RIGHT));
    frame.render_widget(sidebar_menu, sidebar_layout[0]);

    // sidebar navigation hint
    let sidebar_nav_hint = Paragraph::new("\n   [↑↓] Navigate     [q] Quit")
        .block(Block::default().borders(Borders::RIGHT));
    frame.render_widget(sidebar_nav_hint, sidebar_layout[1]);
    
    // detail render
    render_detail(frame, content_layout[1], state.selected);

}