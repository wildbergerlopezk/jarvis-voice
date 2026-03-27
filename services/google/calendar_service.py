class CalendarService:
    def __init__(self):
        self.service = None

    def get_upcoming_events(self, max_results=10):
        return []

    def create_event(self, summary, start_time, end_time):
        print(f"📅 Creando evento: {summary}")
        return True
