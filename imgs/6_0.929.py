d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)

d.end()
