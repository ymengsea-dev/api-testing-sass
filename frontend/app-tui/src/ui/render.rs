use crate::controller::AppState;

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
    let logo: &str ="
    ░█▀█░█▀█░▀█▀░░░█▀▀░█▀█░█▀▀░█▀▀
    ░█▀█░█▀▀░░█░░░░▀▀█░█▀█░▀▀█░▀▀█
    ░▀░▀░▀░░░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀";
    let header = Paragraph::new(logo).block(Block::default().borders(Borders::BOTTOM));
    frame.render_widget(header, main_layout[0]);

    // footer
    let footer = Paragraph::new("[↑↓] Navigate     [q] Quit").block(Block::default().borders(Borders::TOP));
    frame.render_widget(footer, main_layout[2]);

    // body content split
    let content_layout = Layout::default()
        .direction(Direction::Horizontal)
            .constraints([
                Constraint::Percentage(25),
                Constraint::Percentage(75),
            ])
            .split(main_layout[1]);
    
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
    let sidebar = List::new(list_items)
        .block(Block::default().borders(Borders::RIGHT));
    frame.render_widget(sidebar, content_layout[0]);

    let detail = Paragraph::new("Detail")
        .block(Block::default());
    frame.render_widget(detail, content_layout[1]);

}