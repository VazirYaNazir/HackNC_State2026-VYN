export const Colors = {
  white: "#ffffff",
  gray100: "#dddddd",
  gray200: "#cccccc",
  gray500: "#7e7e7e",
  black: "#000000",
} as const;

export const AppColors = {
  background: Colors.black,
  text: Colors.white,
  mutedText: Colors.gray200,
  border: Colors.gray500,
} as const;
