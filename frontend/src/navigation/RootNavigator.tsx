import React from "react";
import { useAuth } from "../auth/AuthContext";
import { AuthStack } from "./AuthStack";
import { AppTabs } from "./AppTabs";

export function RootNavigator() {
  const { user } = useAuth();
  return user ? <AppTabs /> : <AuthStack />;
}
