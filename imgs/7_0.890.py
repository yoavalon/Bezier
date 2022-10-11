d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SE, Length.medium)

d.end()
