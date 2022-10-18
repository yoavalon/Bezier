d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)

d.end()
