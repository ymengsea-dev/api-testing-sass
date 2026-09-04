pub mod app_state;
pub mod key_event;

// Re-export for easier imports elsewhere
pub use app_state::AppState;
pub use key_event::handle_key_events;