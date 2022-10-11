d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)

d.end()
