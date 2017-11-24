#!src/Python-2.7.12/.localpython/bin/python2

'''
<?php

// Set some empty arrays that will contain the names of the files
$files_fasta_basenames = array();
$files_fasta = array();
$files_fastq = array();
$files_otherFiles = array();
$all_files = array();

// Define arrays that contain the file extensions supported for reference sequence and read files
$extensions_fasta = array('.fa');
$extensions_fastq = array('.fq');

// Get in an array all items in 'user_data' directory excluding references
// to self (.) and parent (..) dirs
$user_input_files = array_slice(scandir('../user_data'), 2);
	
// Determine whether there are files with the expected file extensions
foreach ($user_input_files as $name_and_extension) {
	// Get the position (0-based) of last dot in file name
	$last_dot_pos = strrpos($name_and_extension, '.');
	// Get the extension of the file
	$extension = substr($name_and_extension, $last_dot_pos);
	
	// Fill in the different file arrays with the approppriate file names
	if (in_array($extension, $extensions_fasta)) {
		array_push($files_fasta, $name_and_extension);

		// Get the basename of the file
		// Example 1: 1.arabidopsis.fa     Basename = arabidopsis
		// Example 2: TAIR10.fa            Basename = TAIR10
		$name = substr($name_and_extension, 0, $last_dot_pos);
		if (strpos($name, '.') != false) {
			$basename = substr($name, 0, strpos($name, '.'));
		} else {
			$basename = $name;
		}
		array_push($files_fasta_basenames, $basename);
		// Remove duplicates and reset the indexes
		$files_fasta_basenames = array_unique($files_fasta_basenames);
		$files_fasta_basenames = array_values($files_fasta_basenames);
	
	} else if (in_array($extension, $extensions_fastq)) {
		array_push($files_fastq, $name_and_extension);

	} else {
		array_push($files_otherFiles, $name_and_extension);
	}
}

// Create array of arrays and encode it as a JSON object 
array_push($all_files, $files_fasta_basenames, $files_fasta, $files_fastq, $files_otherFiles);
$response = json_encode($all_files);

/*
echo "<pre>";
print_r($all_files);
echo "</pre>";
*/

// Send back JSON object
echo $response;
'''