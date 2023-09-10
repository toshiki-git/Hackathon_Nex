export interface ErrorResponse {
  detail: string;
}

export interface UserDataType {
  id?: number;
  display_name?: string | null;
  username?: string;
  email?: string;
  session_cert?: string;
}
