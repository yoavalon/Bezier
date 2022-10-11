d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
