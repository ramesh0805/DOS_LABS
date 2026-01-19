subjects = ["User1", "User2", "Admin"]
objects = ["File1", "File2", "Printer"]

access_matrix = {
    "User1": {"File1": {"read","write"}, "File2": {"read"}, "Printer": set()},
    "User2": {"File1": {"read"},"File2" : set(), "Printer": {"print"}},
    "Admin": {"File1": {"read","write"}, "File2": {"read","write"}, "Printer": {"print"}}
}

def display_matrix():
  print("\nAccess Matrix:")
  print(f"{'Subject':<10} {'File1':<20} {'File2':<20} {'Printer':<20}")
  for s in subjects:
    print(f"{s:<10} {str(access_matrix[s]['File1']):<20} {str(access_matrix[s]['File2']):<20} {str(access_matrix[s]['Printer']):<20}")

def grant(subject,obj,right):
  access_matrix[subject][obj].add(right)
  print(f"\nGranted {right} access on {obj} to {subject}.")

def revoke(subject,obj,right):
  if right in access_matrix[subject][obj]:
    access_matrix[subject][obj].remove(right)
    print(f"\nRevoked {right} access on {obj} from {subject}.")
  else:
    print(f"\n{subject} does not have {right} access on {obj}.")

def check_access(subject,obj,right):
  if right in access_matrix[subject][obj]:
    print(f"\nAccess granted: {subject} can {right} {obj}.")
  else:
    print(f"\nAccess denied: {subject} cannot {right} {obj}.")

display_matrix()

check_access("User1", "File1", "write")
grant("User2", "File2", "read")
revoke("User1", "File1", "write")
display_matrix()