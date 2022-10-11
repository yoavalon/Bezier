d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
