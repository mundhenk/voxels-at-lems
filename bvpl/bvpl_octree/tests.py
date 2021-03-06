# Temporary tests. 

#In this test
#1. Create Scene
#2. Create kernel vector
#3. Apply kernels to the scene
#4. Display results as disks


#import bvpl_octree_batch;
#bvpl_octree_batch.register_processes();
#bvpl_octree_batch.register_datatypes();
#
#class dbvalue:
#  def __init__(self, index, type):
#    self.id = index    # unsigned integer
#    self.type = type   # string
#
#
#model_dir = "/Users/isa/Experiments/Synthetic";
#output_dir = "/Users/isa/Experiments/Synthetic/edge3d";
#
#
#print("Creating a Scene");
#bvpl_octree_batch.init_process("boxmCreateSceneProcess");
#bvpl_octree_batch.set_input_string(0,  model_dir +"/gaussf1_scene.xml");
#bvpl_octree_batch.run_process();
#(scene_id, scene_type) = bvpl_octree_batch.commit_output(0);
#scene= dbvalue(scene_id, scene_type);
#
#print("*************************************");
#print("Creating 3D edge kernel");
#bvpl_octree_batch.init_process("bvplCreateEdge3dKernelVectorProcess");
#bvpl_octree_batch.set_input_unsigned(0,3);
#bvpl_octree_batch.set_input_unsigned(1,3);
#bvpl_octree_batch.set_input_unsigned(2,3);
#bvpl_octree_batch.run_process();
#(kernel_id,kernel_type)= bvpl_octree_batch.commit_output(0);
#kernel_vector = dbvalue(kernel_id,kernel_type);
#
#print("*************************************");
#print("Running Operator");
#bvpl_octree_batch.init_process("bvplSceneVectorOperatorProcess");
#bvpl_octree_batch.set_input_from_db(0,scene);
#bvpl_octree_batch.set_input_from_db(1,kernel_vector);
#bvpl_octree_batch.set_input_string(2,"bsta_gauss_f1");
#bvpl_octree_batch.set_input_string(3,"max_vector_operator");
#bvpl_octree_batch.set_input_string(4,"gauss_convolution");
#bvpl_octree_batch.set_input_string(5, output_dir);
#bvpl_octree_batch.run_process();
#(out_scene_id,out_scene_type)= bvpl_octree_batch.commit_output(0);
#result_scene = dbvalue(out_scene_id,out_scene_type);
#
#
#print("Writing World");
#bvpl_octree_batch.init_process("bvplSaveVrmlProcess");
#bvpl_octree_batch.set_input_from_db(0,result_scene);
#bvpl_octree_batch.set_input_from_db(1,kernel_vector);
#bvpl_octree_batch.set_input_string(2, output_dir +"/result_scene.wrl");
#bvpl_octree_batch.run_process();

