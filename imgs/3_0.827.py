d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
