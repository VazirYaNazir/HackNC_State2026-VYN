import React from "react";
import { StyleSheet, View, type ViewStyle } from "react-native";
import { AppColors } from "../theme/colors";

type ScreenProps = {
  children: React.ReactNode;
  backgroundColor?: string;
  style?: ViewStyle;
};

const styles = StyleSheet.create({
  base: { flex: 1 },
});

export function Screen({
  children,
  backgroundColor = AppColors.background,
  style,
}: ScreenProps) {
  return <View style={[styles.base, { backgroundColor }, style]}>{children}</View>;
}
