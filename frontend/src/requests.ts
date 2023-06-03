import axios from "axios";

class TimetableApi {
  private api = axios;

  async createTimetableLesson(timetableBody: object) {
    const response = await this.api.post(
      `api/lesson-timetable/`,
      timetableBody
    );
    return response.data;
  }

  async createTimetableEvent(timetableBody: object) {
    const response = await this.api.post(`api/event-timetable/`, timetableBody);
    return response.data;
  }

  async editTimetable(id: number, timetableBody: object) {
    const response = await this.api.put(`api/timetable/${id}/`, timetableBody);
    return response.data;
  }
}

export default new TimetableApi();
