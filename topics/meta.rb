require 'MetaData2'
require 'Upload2'
require 'Shortcuts'
require 'Image2'
require 'Contracts'


meta_object do
  extend MetaData2
  extend Upload2::Actions
  extend Shortcuts::Actions

  inherit_remote_directory 'topics'
end
