d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
