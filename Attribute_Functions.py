can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for data_type in can_we_count_it:
  if hasattr(data_type, "count"):
    print(str(type(data_type)) + "has the count attribute!")
  else:
    print(str(type(data_type)) + " does not have the count attribute :(")