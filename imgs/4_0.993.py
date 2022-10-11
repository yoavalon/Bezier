d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.medium)

d.end()
