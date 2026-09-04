// this is where the application state lives here

pub enum InputMode {
    Normal, // use navigation
    Typing, // typing mode -> use slash command
}

// sidebar state
pub struct AppState {
    pub selected: usize,
    pub items: Vec<&'static str>,
    pub should_quit: bool,
    pub input_mode: InputMode,
    pub input: String,
    pub cursor_position: usize,
}

impl AppState{
    
    pub fn new() -> Self {
        Self {
            selected: 0,
            items : vec![
                "Endpoints",
                "Test Case Library",
                "History",
                "Environment",
                "Help",
            ],
            should_quit: false,
            input_mode: InputMode::Normal,
            input: String::new(),
            cursor_position: 0,
        }
    }

    pub fn enter_char(&mut self, new_char: char){
        let index = self.byte_index();
        self.input.insert(index, new_char);
        self.move_cursor_right();
    }

    pub fn delete_char(&mut self){
        if self.cursor_position != 0 {
            let currect_index = self.cursor_position;
            let from_left_to_current_index = currect_index - 1;

            let before_char_to_delete = self.input.chars().take(from_left_to_current_index);
            let after_char_to_delete = self.input.chars().skip(currect_index);

            self.input = before_char_to_delete.chain(after_char_to_delete).collect();
            self.move_cursor_left();
        }
    }

    pub fn move_cursor_left(&mut self){
        let cursor_moved_left = self.cursor_position.saturating_sub(1);
        self.cursor_position = self.clamp_cursor(cursor_moved_left);
    }

    pub fn move_cursor_right(&mut self){
        let cursor_moved_right =  self.cursor_position.saturating_add(1);
        self.cursor_position = self.clamp_cursor(cursor_moved_right);
    }

    fn clamp_cursor(&self, new_cursor_position: usize) -> usize {
        new_cursor_position.clamp(0, self.input.chars().count())
    }

    fn byte_index(&self) -> usize {
        self.input
            .char_indices()
            .map(|(i, _)| i)
            .nth(self.cursor_position)
            .unwrap_or(self.input.len())
    }

    pub fn next(&mut self){
        if self.selected < self.items.len() - 1 {
            self.selected += 1;
        }
    }

    pub fn prev(&mut self){
        if self.selected > 0 {
            self.selected -= 1;
        }
    }

    pub fn quit(&mut self){
        self.should_quit = true;
    }
}