d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)

d.end()
