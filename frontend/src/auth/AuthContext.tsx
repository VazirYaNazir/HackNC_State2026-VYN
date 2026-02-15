import React, { createContext, useContext, useMemo, useState } from "react";

type User = { id: string; name: string } | null;

type AuthContextValue = {
  user: User;
  signIn: (name?: string) => void;
  signOut: () => void;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User>(null);

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      signIn: (name = "User") => setUser({ id: "1", name }),
      signOut: () => setUser(null),
    }),
    [user]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}
