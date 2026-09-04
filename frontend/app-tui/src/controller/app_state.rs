// this is where the application state lives here

// sidebar state
pub struct AppState {
    pub selected: usize,
    pub items: Vec<&'static str>,
    pub should_quit: bool,
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
        }
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