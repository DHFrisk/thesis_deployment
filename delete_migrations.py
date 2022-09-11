import os
current_path= os.getcwd()

for i in os.listdir(current_path):
   if os.path.isdir(i):
      temporal_path=os.path.join(current_path, i)
      for j in os.listdir(temporal_path):
         if j == "migrations":
            migrations_path= os.path.join(temporal_path, j)
            if os.path.isdir(migrations_path):
               for k in os.listdir(migrations_path):
                  temporal_path_1= os.path.join(migrations_path,k)
                  if os.path.isfile(temporal_path_1):
                     if os.path.basename(temporal_path_1) != "__init__.py":
                        os.remove(temporal_path_1)
